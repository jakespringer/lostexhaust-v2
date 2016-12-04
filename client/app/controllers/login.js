'use strict';

angular.module('lostexhaust')
.controller('LoginController', ['$scope', '$rootScope', '$routeParams', '$location', 'lostexhaustService', LoginController]);

function LoginController($scope, $rootScope, $routeParams, $location, lostexhaustService) {
  $scope.displayReady = false;

  if ($routeParams.token) {
    $rootScope.token = $routeParams.token;
    lostexhaustService.checkToken($rootScope.token, function (response) {
      if (response.data.user_id) {
        $scope.validToken = true;
        lostexhaustService.setToken($rootScope.token);
        setCookie('token', $rootScope.token, 1);
        $location.url('/');
        $scope.displayReady = true;
      }
    }, function (error) {
      window.location.href = "https://inside.catlin.edu/api/lostexhaust/login.py";
    });
  } else {
    window.location.href = "https://inside.catlin.edu/api/lostexhaust/login.py";
  }
}
