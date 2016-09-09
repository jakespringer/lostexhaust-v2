'use strict';

angular.module('lostexhaust')

.service('lostexhaustService', ['$http', function ($http) {
  var ROOT_URL = 'http://localhost:5000';

  return {
    token: null,

    setToken: function (newToken) {
      this.token = newToken;
      return this.token;
    },

    getToken: function () {
      return this.token;
    },

    getPersonInfo: function (personId, callback, error) {
      $http({
        method: 'POST',
        url: ROOT_URL + '/api/person/info/' + personId + '.json',
        headers: {
          'Content-Type': 'text/plain'
        },
        data: {
          token: this.getToken()
        }
      }).then(callback, error);
    },

    getPersonEverything: function (personId, callback, error) {
      $http({
        method: 'POST',
        url: ROOT_URL + '/api/person/everything/' + personId + '.json',
        headers: {
          'Content-Type': 'text/plain'
        },
        data: {
          token: this.getToken()
        }
      }).then(callback, error);
    },

    getHouseholdInfo: function (householdId, callback, error) {
      $http({
        method: 'POST',
        url: ROOT_URL + '/api/household/info/' + householdId + '.json',
        headers: {
          'Content-Type': 'text/plain'
        },
        data: {
          token: this.getToken()
        }
      }).then(callback, error);
    },

    getHouseholdEverything: function (householdId, callback, error) {
      $http({
        method: 'POST',
        url: ROOT_URL + '/api/household/everything/' + householdId + '.json',
        headers: {
          'Content-Type': 'text/plain'
        },
        data: {
          token: this.getToken()
        }
      }).then(callback, error);
    },

    getCarpool: function (originId, targetId, callback, error) {
      $http({
        method: 'POST',
        url: ROOT_URL + '/api/carpool/' + originId + '.json?target='+targetId,
        headers: {
          'Content-Type': 'text/plain'
        },
        data: {
          token: this.getToken()
        }
      }).then(callback, error);
    },

    getCarpoolsNear: function (originId, results, callback, error) {
      $http({
        method: 'POST',
        url: ROOT_URL + '/api/carpool/near/' + originId + '.json?results=' + results,
        headers: {
          'Content-Type': 'text/plain'
        },
        data: {
          token: this.getToken()
        }
      }).then(callback, error);
    },

    checkToken: function (token, callback, error) {
      $http({
        method: 'GET',
        url: ROOT_URL + '/api/auth/check.json?token='+token,
      }).then(callback, error);
    }
  };
}]);
