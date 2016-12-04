'use strict';

angular.module('lostexhaust')
.controller('HouseholdController', ['$scope', '$rootScope', '$routeParams', '$sce', 'lostexhaustService', HouseholdController]);

function HouseholdController($scope, $rootScope, $routeParams, $sce, lostexhaustService) {
  $scope.address = "";
  $scope.maps_address = "";
  $scope.displayReady = false;

  lostexhaustService.checkToken($rootScope.token, function (response) {
    if (!response.data.success) window.location.href = "https://inside.catlin.edu/api/lostexhaust/login.py";
    if (response.data.user_id) {
      lostexhaustService.setToken($rootScope.token);
      lostexhaustService.getHouseholdEverything($routeParams.h, function (result) {
        $scope.address = result.data.full_address;
        $scope.maps_address = $sce.trustAsResourceUrl("https://www.google.com/maps/embed/v1/place?key=AIzaSyD_DoQ4FFyAG-98-96ygUuPRIoU2bzu9c4&q=place_id:" + result.data.place_id);
        $scope.inhabitants = result.data.inhabitants;
        $scope.displayReady = true;
      }, function (error) {
        // error
      });
    }
  }, function (error) {
    window.location.href = "https://inside.catlin.edu/api/lostexhaust/login.py";
  });
}
