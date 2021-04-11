var mongo      = require('mongodb'),
    mongoStore = require('connect-mongodb');

var mongo_config = {
  host:     "staff.mongohq.com",
  port:     10004,
  dbname:   "appXXX",
  username: "italk",
  password: "Anhhuy123"};

var app = module.exports = express.createServer();

app.configure(function() {
  // ...
  app.use(express.session({
    secret:  "...",
    store:   new mongoStore({
      server_config: new mongo.Server(mongo_config.host, mongo_config.port,
                       {auto_reconnect: true, native_parser: true}),
      dbname:        mongo_config.dbname,
      username:      mongo_config.username,
      password:      mongo_config.password}),
    cookie: {maxAge: 604800000},
  }));
  // ...
});