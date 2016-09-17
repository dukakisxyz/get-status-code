<h1> get-status-code </h1>
<p>A bitcoin payable API that checks the http status code of a given website</p>

<h3> How to use: </h3>
<p>This service returnes the HTTP status code of a given website, in exchange for bitcoin</p>
<p> To check a website run: </p>

<pre><code>21 buy http://[fcce:a977:ee7d:817b:3380:0000:0000:0001]:4000/check_website/"website's address"
</code></pre>
<p> For example: </p>
<pre><code>21 buy http://[fcce:a977:ee7d:817b:3380:0000:0000:0001]:4000/check_website/www.google.com
</code></pre>

<p> Important note: Don't add "http://" or "https://" in the beginning of the web address, 
otherwise you will break the operation. </p>

<p>Then you will receive a json string in the form of dictionary with the status code and its description</p>
<pre><code> {
    "200": "OK"
}
</code></pre>

<h3> Requirements </h3>

1. A  <a href="https://21.co">21 Bitcoin Computer</a> or 21 installed on AWS or MacOS
2. You need to be connected to the 21 Network
