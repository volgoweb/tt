
var app = angular.module('task', []);
app.task_item_css_class = 'tasks-list__item';
app.task_detail_css = '.tasks__task-detail';

app.controller('tasksList', function($scope, $http) {
  $http.get('/task/rest/').success(function(data) {
    $scope.tasks = {};
    $.each(data, function(i, el) {
      $scope.tasks[el.id] = el;
    });
  });

  $http.get('/task/get-models/').success(function(data) {
    $scope.models = data;
  });


  this.edit = function(task_id) {
  };

  this.showDetailTask = function(task_id) {
    $scope.chosen_task = $scope.tasks[task_id];
    console.log($scope.chosen_task);
  };

  // this.changeCompleted = function(task_id, status) {
  // };

  this.setModelFieldTitle = function(task, field_name) {
      var value = task[field_name]['value'];
      task[field_name]['title'] = task[field_name].choices[value];
  };

  this.saveTask = function(task) {
    var csrf = global_ajax_csrf.getCookie('csrftoken');
    $http.defaults.headers.post['X-CSRFToken'] = csrf;
    $http.defaults.headers.put['X-CSRFToken'] = csrf;
    // TODO добавить для всех аякс-загрузок заставку-ожидание
    $http.put('/task/rest/' + task.id, task).success(function(data) {
        $scope.tasks[task.id] = data
        $scope.taskDetailForm.$setPristine();
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
