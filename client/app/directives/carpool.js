'use strict';

angular.module('lostexhaust')

.controller('CarpoolController', ['$scope', '$rootScope', 'lostexhaustService', function ($scope, $rootScope, lostexhaustService) {
  $scope.doneLoading = false;
  $scope.carpool = null;
  $scope.token = $rootScope.token;
  $scope.onLoad = function (origin, target, distance) {
    $scope.distanceFormatted = parseFloat(distance).toFixed(1);
    lostexhaustService.getHouseholdEverything(target, function (response) {
      $scope.carpool = response.data;
      $scope.doneLoading = true;
    }, function (error) {
    });
  }
}])

.directive('carpool', ['lostexhaustService', function (lostexhaustService) {
  return {
    templateUrl: 'templates/carpool.html',
    restrict: 'E',
    scope: {
      origin: '@origin',
      target: '@target',
      distance: '@distance'
    },
    link: function(scope, element, attrs, controllers) {
      scope.onLoad(attrs.origin, attrs.target, attrs.distance);
    },
    controller: 'CarpoolController'
  }
}]);
