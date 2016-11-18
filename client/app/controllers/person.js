'use strict';

angular.module('lostexhaust')
.controller('PersonController', ['$scope', '$rootScope', '$routeParams', '$sce', 'lostexhaustService', PersonController]);

function PersonController($scope, $rootScope, $routeParams, $sce, lostexhaustService) {
  $scope.person = {};

  lostexhaustService.checkToken($rootScope.token, function (response) {
    if (response.data.user_id) {
      $scope.validToken = true;
      lostexhaustService.setToken($rootScope.token);
      lostexhaustService.getPersonEverything($routeParams.p, function (result) {
        console.log(result.data);
        $scope.person = result.data;
      }, function (error) {
        // error
      });
    }
  }, function (error) {
    alert("Failed to login.")
  });
}
