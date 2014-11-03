
var app = angular.module('task', []);
app.task_item_css_class = 'tasks-list__item';
app.task_detail_css = '.tasks__task-detail';
app.base_url = '/tasks/';
app.base_rest_url = app.base_url + 'rest/';

app.controller('tasksList', function($scope, $http) {
  $http.get(app.base_rest_url).success(function(data) {
    $scope.tasks = {};
    $scope.main = main;
    console.log($scope.main.helper);

    $.each(data, function(i, el) {
      $scope.tasks[el.id] = el;
    });
  });

  $http.get(app.base_url + 'get-models/').success(function(data) {
    $scope.models = data;
  });


  this.showDetailTask = function(task_id) {
    $scope.chosen_task = $scope.tasks[task_id];
    $scope.chosen_task.view_mode = 'view';
    console.log($scope.chosen_task);
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
    });
  };

  this.runAction = function(task_id, action_name) {
    $http.get(app.base_rest_url + task_id + '/run_action/?action=' + action_name).success(function(data) {
        $scope.chosen_task = $scope.tasks[task_id] = data
    });
  };
});

// app.filter('completedTaskCheckbox', function () {
//   return function (input) {
//     if (input === 'widescreen') {
//       return '270px';
//     } else {
//       return '360px';
//     }
//   };
// });
