var amqp = require("amqplib/callback_api");

amqp.connect("amqp://localhost", function (error0, connection) {
  if (error0) {
    throw error0;
  }
  connection.createChannel(function (error1, channel) {
    if (error1) {
      throw error1;
    }
    var exchange = "direct_logs";
    var args = process.argv.slice(2);
    var msg = args.join(" ") || "Hello World!";

    channel.assertExchange(exchange, "direct", {
      durable: false,
    });

    rk = ["T1", "T2"];
    rk.forEach((element) => {
      channel.publish(exchange, element, Buffer.from(msg));
      console.log(" [x] Sent %s: '%s'", element, msg);
    });
  });

  setTimeout(function () {
    connection.close();
    process.exit(0);
  }, 500);
});
