const Greeter = artifacts.require("./Migrations.sol");

module.exports = function(deployer) {
  deployer.deploy(Greeter);
};
