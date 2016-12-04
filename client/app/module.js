'use strict';

angular.module('lostexhaust', ['ngRoute'])

.config(['$locationProvider', '$routeProvider', function($locationProvider, $routeProvider) {
  $locationProvider.hashPrefix('');
  $routeProvider.otherwise({redirectTo: '/carpools'});
}])

.run(['$rootScope', function($rootScope, lostexhaustService) {
  $rootScope.token = getCookie('token');
  $rootScope.currentScroll = 0;
  window.onscroll = (function () {
    $rootScope.currentScroll = document.documentElement.scrollTop || document.body.scrollTop;
  });
}]);

function bound(val, lower, upper) {
  val = val|0;
  lower = lower|0;
  upper = upper|0;
  if (lower > upper) {
    lower ^= upper;
    upper ^= lower;
    lower ^= upper;
  }
  if (val > upper) {
    return upper;
  } else if (val < lower) {
    return lower;
  } else {
    return val;
  }
}

function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length,c.length);
        }
    }
    return "";
}

