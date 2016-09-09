'use strict';

angular.module('lostexhaust')

.config(['$routeProvider', function ($routeProvider) {
  $routeProvider.when('/user', {
    templateUrl: 'templates/user.html',
    controller: 'UserController'
  });
}])
