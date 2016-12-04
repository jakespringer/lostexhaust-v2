'use strict';

angular.module('lostexhaust')

.config(['$routeProvider', function ($routeProvider) {
  $routeProvider.when('/login', {
    template: 'Logging in... please wait to be redirected.',
    controller: 'LoginController'
  });
}])
