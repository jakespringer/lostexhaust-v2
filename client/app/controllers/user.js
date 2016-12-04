'use strict';

angular.module('lostexhaust')
.controller('UserController', ['$scope', '$rootScope', '$routeParams', '$sce', 'lostexhaustService', UserController]);

function UserController($scope, $rootScope, $routeParams, $sce, lostexhaustService) {
  $scope.person = {};
  $scope.displayReady = false;

  lostexhaustService.checkToken($rootScope.token, function (response) {
    if (!response.data.success) window.location.href = "https://inside.catlin.edu/api/lostexhaust/login.py";
    if (response.data.user_id) {
      $scope.validToken = true;
      lostexhaustService.setToken($rootScope.token);
      lostexhaustService.getPersonEverything(response.data.user_id, function (result) {
        $scope.person = result.data;
        $scope.displayReady = true;
      }, function (error) {
        // error
      });
    }
  }, function (error) {
    window.location.href = "https://inside.catlin.edu/api/lostexhaust/login.py";
  });
}
