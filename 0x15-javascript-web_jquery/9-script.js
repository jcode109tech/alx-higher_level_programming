const $ = window.$;
const url = "https://hellosalut.stefanbohacek.dev/?lang=fr";

$.get(url, function(body) {
  let hello = body["hello"];
  $("#hello").html(hello);
});
