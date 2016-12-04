'use strict';

angular.module('lostexhaust')
.controller('CarpoolsController', ['$scope', '$rootScope', 'lostexhaustService', CarpoolsController]);

function CarpoolsController($scope, $rootScope, lostexhaustService) {
  $scope.ready = false;
  $scope.sorted = [];
  $scope.user = {};
  $scope.validToken = true;
  $scope.numRequesting = 10;
  $scope.displayReady = false;

  $scope.refreshCarpools = function (numCarpools) {
    $scope.displayReady = false;
    $scope.numRequesting = Math.max(numCarpools, 10);
    lostexhaustService.checkToken($rootScope.token, function (response) {
      if (!response.data.success) window.location.href = "https://inside.catlin.edu/api/lostexhaust/login.py";
      if (response.data.user_id) {
        $scope.validToken = true;
        lostexhaustService.setToken($rootScope.token);
        lostexhaustService.getPersonEverything(response.data.user_id, function (response) {
          if (response.data.eeid) {
            $scope.user = response.data;
            $scope.currentlySelectedHousehold = $scope.user.households[0];
            lostexhaustService.getCarpoolsNear($scope.currentlySelectedHousehold.household_id, $scope.numRequesting, function (response) {
              $scope.displayReady = true;
              if (response.data instanceof Array) {
                $scope.sorted = response.data;
                $scope.ready = true;
              }
            }, function (error) {
              $scope.ready = true;
            });
          }
        }, function (error) {
          $scope.ready = true;
        });
      } else {
        window.location.href = "https://inside.catlin.edu/api/lostexhaust/login.py";
      }
    }, function (error) {
      $scope.ready = true;
    });
  };

  $scope.refreshCarpoolsAndScroll = function (numCarpools) {
    $scope.refreshCarpools(numCarpools);
    document.documentElement.scrollTop = document.body.scrollTop = $rootScope.currentScroll;
  };

  $scope.refreshCarpools(10);
}
