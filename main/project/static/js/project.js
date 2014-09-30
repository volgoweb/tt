
var app = angular.module('project', []);
app.controller('projects', function($scope, $http) {
    $http.get('/project/json/').success(function(data) {
        $scope.projects = data;
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

app.controller('projectItem', function() {
    this.click = function(css_id) {
        var $pitem = $(css_id);
        if ($pitem.hasClass('edit')) {
            $pitem.removeClass('edit');
            $pitem.css('background-color', 'transparent');
        }
        else {
            $pitem.addClass('edit');
            $pitem.css('background-color', 'yellow');
        }
    };

    this.blur = function(css_id) {
        var $pitem = $(css_id);
    };
});

// app.controller('projects', function($scope, $http) {
//     $http.put('/project/json/').success(function(data) {
//         $scope.projects = data;
//     });
// });
