'use strict';

angular.module('lostexhaust')

.config(['$routeProvider', function ($routeProvider) {
  $routeProvider.when('/home', {
    templateUrl: 'templates/home.html',
    controller: 'HomeController'
  });
}])
