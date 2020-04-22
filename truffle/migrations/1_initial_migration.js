const Greeter = artifacts.require("./greeter.sol");

module.exports = function(deployer) {
  deployer.deploy(Greeter);
};
