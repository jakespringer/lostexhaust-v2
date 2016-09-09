'use strict';

angular.module('lostexhaust', ['ngRoute'])

.config(['$locationProvider', '$routeProvider', function($locationProvider, $routeProvider) {
  $locationProvider.hashPrefix('');
  $routeProvider.otherwise({redirectTo: '/carpools'});
}])

.run(['$rootScope', function($rootScope) {
  $rootScope.token = "0B204F9A20C594BE6ADF2DFF903D458AC1A0BE55273D91082CC6DD1C268ADA27A4EC556DCF0001CD2A7F73F125014252C3BE3AFD0B08AF185C4A5EFAA60B91EB614DF3FFF7AF1728447EE55E4FC07391CD40B0178FE7C23EF736C9D9269FA9A80BD974C8F2647E322F896A2ECA6BD93A14FA9C8570E7232FE70F81362951C5C852DC488A4B5802356CEB76934ACF0958F77495970CED632F940B4C019788B50A69EA4C35FB4E1AD75DF3EF4543B0C99D41A42B32104D48BBEE8BD3B318082BFCA9421055E1AC7413290E956743CAA280A6FE0CF3B47A83B3DFBE98778FB7852D3571EC34A7082A7BBBA14F473790A2632208CB641180FE99BB320EA3616CA436";
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
