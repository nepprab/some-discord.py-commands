const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
console.log(`Logged in as ${client.user.tag}!`);
console.log("Streamstatus by Pro_Gamer368")

client.user.setActivity(`-help`, {
type: "STREAMING",
url: "https://twitch.tv/progamer368ismyowner"})
    .then(presence => console.log(`Your Status has been set to  ${presence.game ? presence.game.none : 'Streaming'}`))
    .catch(console.error);
});

client.login('NzUzMTE5MTAxMTM1NzQ5MTcw.X1hi0Q.qM2lK4sVBCJ6H1vG2UQtcZjx-g0');