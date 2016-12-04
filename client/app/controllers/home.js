'use strict';

angular.module('lostexhaust')
.controller('HomeController', ['$scope', '$rootScope', '$routeParams', '$sce', 'lostexhaustService', HomeController]);

function HomeController($scope, $rootScope, $routeParams, $sce, lostexhaustService) {
  $scope.address = "";
  $scope.maps_address = "";
  $scope.households = [];
  $scope.displayReady = false;

  $scope.refreshHousehold = function (index) {
    $scope.displayReady = false;
    lostexhaustService.checkToken($rootScope.token, function (response) {
      if (!response.data.success) window.location.href = "https://inside.catlin.edu/api/lostexhaust/login.py";
      if (response.data.user_id) {
        $scope.validToken = true;
        lostexhaustService.setToken($rootScope.token);
        lostexhaustService.getPersonEverything(response.data.user_id, function (result) {
          $scope.households = result.data.households;
          lostexhaustService.getHouseholdEverything($scope.households[index].household_id, function (result) {
            $scope.currentlySelectedHousehold = result.data;
            $scope.address = result.data.full_address;
            $scope.maps_address = $sce.trustAsResourceUrl("https://www.google.com/maps/embed/v1/place?key=AIzaSyD_DoQ4FFyAG-98-96ygUuPRIoU2bzu9c4&q=place_id:" + result.data.place_id);
            $scope.inhabitants = result.data.inhabitants;
            $scope.displayReady = true;
          }, function (error) {
            // error
          });
        }, function (error) {
          // error
        });
      }
    }, function (error) {
      window.location.href = "https://inside.catlin.edu/api/lostexhaust/login.py";
    });
  };

  $scope.refreshHousehold(0);
}
