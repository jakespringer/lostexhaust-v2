'use strict';

angular.module('lostexhaust')

.filter('shouldShowPicture', function () {
  return function (input) {
    var out = []; 
    for (var i=0; i<input.length; ++i) {
      if (input[i].affiliation.indexOf('Student') !== -1 || input[i].affiliation.indexOf('Faculty') !== -1) {
        out.push(input[i]);
      }
    }
    return out;
  }
})

.controller('CarpoolController', ['$scope', '$rootScope', 'lostexhaustService', 'shouldShowPictureFilter', function ($scope, $rootScope, lostexhaustService, shouldShowPictureFilter) {
  $scope.doneLoading = false;
  $scope.carpool = null;
  $scope.token = $rootScope.token;
  $scope.onLoad = function (origin, target, distance) {
    $scope.distanceFormatted = parseFloat(distance).toFixed(1);
    lostexhaustService.getHouseholdEverything(target, function (response) {
      $scope.carpool = response.data;
      $scope.filteredInhabitants = shouldShowPictureFilter($scope.carpool.inhabitants);
      $scope.doneLoading = true;
      $scope.displayReady = true;
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
