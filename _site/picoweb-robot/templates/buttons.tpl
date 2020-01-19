{% args req %}
<html>
    <head> 
        <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="icon" href="data:,"> 
        <style>
        html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
        h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}
        .button{display: inline-block; background-color: #e7bd3b; border: none; 
        border-radius: 4px; color: white; padding: 16px 40px; 
        text-decoration: none; font-size: 30px;
        margin: 2px; cursor: pointer;}
        .buttonStop{background-color: red;}
        </style>
    </head>
    <body> 
        <h1>ESP Web Server</h1> 
        {% if req.path[7:] == ""%}
        <p>Robot state: <strong>stop</strong></p>
        {% else %}
        <p>Robot state: <strong>{{req.path[7:]}}</strong></p>
        {% endif %}
        <p><a href="/robot=stop"><button class="button buttonStop">STOP</button></a></p>
        <p><a href="/robot=forward"><button class="button">FORWARD</button></a></p>
        <p><a href="/robot=backward"><button class="button">BACKWARD</button></a></p>
        <p><a href="/robot=right"><button class="button">RIGHT</button></a></p>
        <p><a href="/robot=left"><button class="button">LEFT</button></a></p>
    </body>
</html>


