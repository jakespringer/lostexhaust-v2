'use strict';

angular.module('lostexhaust')

.config(['$routeProvider', function ($routeProvider) {
  $routeProvider.when('/admin_panel', {
    templateUrl: 'templates/admin_panel.html',
    controller: 'AdminPanelController'
  });
}])
