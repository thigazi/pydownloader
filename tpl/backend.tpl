<!DOCTYPE HTML>
<html>
    <head>
        <title>Backend</title>
        <script src="/js/jquery-2.2.3.min.js" type="text/javascript"></script>        
        <script src="/js/backend.js" type="text/javascript"></script>             
        <style type="text/css">        
        #MainX {position:relative;left:5%; margin-left:-X;width:800px;top:50px;font-family:Arial;}
        #MainX ul{list-style-type: none;padding:0px;width:150px;}
        #MainX ul li {cursor:pointer;}
        #MainX ul li:hover {color:#ef2929;}
        
        #MainX #left {position:absolute;}
        #MainX #right {position:absolute;left:200px;}
        #MainX #right button {border-style:solid;border-width:1px;border-color:#000000;cursor:pointer;}
        #MainX #right button:hover {border-style:dashed;border-width:2px;border-color:#ef2929;}
        </style>        
    </head>
    <body>
        <img src="/img/logout.svg" width="20px" height="20">                                
        <div id="MainX">                        
            <div id="left">            
            <b>Generierte Codes</b><br>
            <ul>
                <!--<li style="color:#ef2929;" onclick="MeinObj.GetInfo('SKJKJK');">SKJKJK</li>-->
                <li onclick="BackendObj.GetInfo('SKJKJK');">SKJKJK</li>
                <li onclick="BackendObj.GetInfo('alkwAKJK');">alkwAKJK</li>
                <li onclick="BackendObj.GetInfo('woikAMKJ');">woikAMKJ</li>                
            </ul>
            </div>
            <div id="right">
                {% block stuff %}
                {% endblock %}
                <!--                
                <b>Filelist</b><br>
                Anzahl der Dateien in der DB: 10
                <form accept-charset="UTF-8" style="margin-bottom: 10px;">
                <table>
                    <thead></thead>
                    <tbody>
                        <tr>
                        <td>MeineDatei.zip</td><td>Downloads: <select><option value="0">1</option><option value="1">1</option><option selected="selected" value="2">2</option><option value="3">3</option></select></td><td><img src="/img/delete.svg" width="20px" height="20"></td>
                    </tr>                        
                    </tbody>                                                            
                </table>
                <input type="file" />                
                </form>
                <span><button>L&ouml;sche Code</button></span>
                -->                
                <span><button>Neuer Code</button></span>                                
            </div>            
        </div>                          
    </body>
</html>