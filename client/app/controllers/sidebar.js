'use strict';

angular.module('lostexhaust')
.controller('SidebarController', ['$scope', '$rootScope', '$routeParams', '$sce', 'lostexhaustService', SidebarController]);

function SidebarController($scope, $rootScope, $routeParams, $sce, lostexhaustService) {
  $rootScope.rootDisplayReady = false;
  $scope.displayReady = false;
  lostexhaustService.checkToken($rootScope.token, function (response) {
    if (response.data.success) {
      lostexhaustService.setToken($rootScope.token);
      lostexhaustService.getPersonInfo(response.data.user_id, function (result) {
        $scope.user = result.data;
        $rootScope.rootDisplayReady = true;
        $scope.displayReady = true;
      }, function (error) {
      });
    }
  }, function (error) {
    // error
  });

  $scope.logout = function () {
    document.cookie = 'token' + '=; expires=Thu, 01 Jan 1970 00:00:01 GMT;';
    window.location = 'https://inside.catlin.edu/api/lostexhaust/login.py';
  };
}
