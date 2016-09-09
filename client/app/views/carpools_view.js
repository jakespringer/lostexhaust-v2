'use strict';

angular.module('lostexhaust')

.config(['$routeProvider', function ($routeProvider) {
  $routeProvider.when('/carpools', {
    templateUrl: 'templates/carpools.html',
    controller: 'CarpoolsController'
  });
}])
