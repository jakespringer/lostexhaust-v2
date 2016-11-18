'use strict';

angular.module('lostexhaust')
.controller('UserController', ['$scope', '$rootScope', '$routeParams', '$sce', 'lostexhaustService', UserController]);

function UserController($scope, $rootScope, $routeParams, $sce, lostexhaustService) {
  $scope.person = {};

  lostexhaustService.checkToken($rootScope.token, function (response) {
    if (response.data.user_id) {
      $scope.validToken = true;
      lostexhaustService.setToken($rootScope.token);
      lostexhaustService.getPersonEverything(response.data.user_id, function (result) {
        $scope.person = result.data;
      }, function (error) {
        // error
      });
    }
  }, function (error) {
    alert("Failed to login.")
  });
}
