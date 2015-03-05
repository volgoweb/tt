
var app = angular.module('project', []);
app.project_item_css_class = 'projects-list__item';
app.project_detail_css = '.projects__project-detail';
app.base_url = '/projects/';
app.base_rest_url = app.base_url + 'rest/';

app.controller('projectsList', function($scope, $http) {
    $http.get(app.base_rest_url).success(function(data) {
        $scope.projects = data.results;
        console.log($scope.projects);
    });


    // $scope.projects = [
    //     {
    //         'pk': 1,
    //         'title': 'First project',
    //     },
    //     {
    //         'pk': 2,
    //         'title': 'Second project',
    //     }
    // ]
});

// app.controller('projectItem', function() {
//     this.click = function(css_id) {
//         var $pitem = $(css_id);
//         if ($pitem.hasClass('edit')) {
//             $pitem.removeClass('edit');
//             $pitem.css('background-color', 'transparent');
//         }
//         else {
//             $pitem.addClass('edit');
//             $pitem.css('background-color', 'yellow');
//         }
//     };
// 
//     this.blur = function(css_id) {
//         var $pitem = $(css_id);
//     };
// });

// app.controller('projects', function($scope, $http) {
//     $http.put('/project/json/').success(function(data) {
//         $scope.projects = data;
//     });
// });
