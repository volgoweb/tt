
var app = angular.module('task', []);
app.task_item_css_class = 'tasks-list__item';
app.task_detail_css = '.tasks__task-detail';
app.base_url = '/tasks/';
app.base_rest_url = app.base_url + 'rest/';

app.controller('tasksList', function($scope, $http) {
    var controller = this;

    $http.get(app.base_url + 'get-models/').success(function(data) {
        $scope.models = data;
        console.log($scope.models);
    });


    $scope.main = main;
    $scope.new_task_initial = {
        priority: {
            value: 0,
        },
    };
    $scope.new_task = angular.copy($scope.new_task_initial)
    $scope.chosen_task = null;
    $scope.addTaskFormVisible = false;
    $scope.active_tasks_list = 'wait_reaction';
    $scope.tasksListsNames = [
        'wait_reaction',
        'my_in_work',
        'in_queue',
        'all',
    ]


    this.showDetailTask = function(task_id) {
        $scope.chosen_task = $scope.tasks[task_id];
        $scope.chosen_task.view_mode = 'view';
        console.log($scope.chosen_task, 'show_chosen_task');
    };

    this.closeDetailTask = function() {
        $scope.chosen_task = null;
    };

    this.setModelFieldTitle = function(task, field_name) {
        var value = task[field_name]['value'];
        task[field_name]['title'] = task[field_name].choices[value];
    };

    this.saveTask = function(task) {
        var csrf = global_ajax_csrf.getCookie('csrftoken');
        $http.defaults.headers.post['X-CSRFToken'] = csrf;
        $http.defaults.headers.put['X-CSRFToken'] = csrf;
        // TODO добавить для всех аякс-загрузок заставку-ожидание
        $http.put(app.base_rest_url + task.id, task).success(function(data) {
            $scope.tasks[task.id] = data
            $scope.taskDetailForm.$setPristine();
            $scope.chosen_task.view_mode = 'view';
            
            // обновим данные о кол-ве задач в каждом списке
            controller.updateTasksListsCount();
            // обновим текущий список
            controller.showTasksList($scope.active_tasks_list);
        });
    };


    this.showAddTask = function() {
        $scope.addTaskFormVisible = true;
    };

    this.addTask = function(task) {
        var that = this;
        var csrf = global_ajax_csrf.getCookie('csrftoken');
        $http.defaults.headers.post['X-CSRFToken'] = csrf;
        $http.defaults.headers.put['X-CSRFToken'] = csrf;
        // TODO добавить для всех аякс-загрузок заставку-ожидание
        $http.post(app.base_rest_url, task).success(function(data) {
            $scope.addTaskFormVisible = false;
            // TODO разобраться, как обнулять форму
            $scope.taskAddForm.$setPristine();
            // $scope.taskAddForm.$dirty = false;
            // $scope.taskAddForm.$pristine = true;
            // $scope.taskAddForm.$submitted = false;
            $scope.new_task = angular.copy($scope.new_task_initial)
            
            // обновим данные о кол-ве задач в каждом списке
            controller.updateTasksListsCount();
            // обновим текущий список
            controller.showTasksList($scope.active_tasks_list);
        });
    };

    this.runAction = function(task_id, action_name) {
        $http.get(app.base_rest_url + task_id + '/run_action/?action=' + action_name).success(function(data) {
            $scope.chosen_task = $scope.tasks[task_id] = data
            $scope.chosen_task.view_mode = 'view';

            // обновим данные о кол-ве задач в каждом списке
            controller.updateTasksListsCount();
            // обновим текущий список
            controller.showTasksList($scope.active_tasks_list);
        });
    };

    /**
     * Заполняет переменную, хранящую список задач текущей вкладки.
     * Соответственно сама таблица обновляется.
     */
    this.setCurrentTasksList = function(tasks_list) {
        $scope.tasks = {};
        $.each(tasks_list, function(i, el) {
            $scope.tasks[el.id] = el;
        });
    }

    /**
     * Обновляет количество задач указанного списка.
     */
    this.showTasksListCount = function(tasks_list_name) {
        // TODO проверять есть ли указанное имя списка в $scope.tasksListsNames
        $http.get(app.base_rest_url + 'tasks_list_count/?tasks_list_name=' + tasks_list_name).success(function(data) {
            $scope[tasks_list_name + '_count'] = data;
        });
    };

    /**
     * Обновляет массив задач указанного списка.
     */
    this.showTasksList = function(tasks_list_name) {
        // TODO проверять есть ли указанное имя списка в $scope.tasksListsNames
        $http.get(app.base_rest_url + 'tasks_list/?tasks_list_name=' + tasks_list_name).success(function(data) {
            controller.setCurrentTasksList(data.results);
            $scope.active_tasks_list = tasks_list_name;
            // очищаем выбранную для детального просмотра задачу
            if ($scope.chosen_task !== null) {
                if ($scope.tasks[$scope.chosen_task.id] === 'undefined') {
                    $scope.chosen_task = null;
                }
            }
        });
    };

    /**
     * Обновляет количество задач у всех списков задач.
     */
    this.updateTasksListsCount = function() {
        for (i in $scope.tasksListsNames) {
            controller.showTasksListCount($scope.tasksListsNames[i]);
        }
    };

    // Показываем дефолтный список задач
    this.showTasksList($scope.active_tasks_list);
    // обновим данные о кол-ве задач в каждом списке
    this.updateTasksListsCount();

    setInterval(function() {
        // обновим данные о кол-ве задач в каждом списке
        controller.updateTasksListsCount();
        // Показываем дефолтный список задач
        controller.showTasksList($scope.active_tasks_list);
    }, 60000);
});
