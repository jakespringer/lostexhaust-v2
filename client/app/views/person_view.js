'use strict';

angular.module('lostexhaust')

.config(['$routeProvider', function ($routeProvider) {
  $routeProvider.when('/person', {
    templateUrl: 'templates/person.html',
    controller: 'PersonController'
  });
}])
