'use strict';

angular.module('lostexhaust')

.config(['$routeProvider', function ($routeProvider) {
  $routeProvider.when('/household', {
    templateUrl: 'templates/household.html',
    controller: 'HouseholdController'
  });
}])
