<!DOCTYPE HTML>
<html>
    <head>
        <title>Backend {%if cid.0 == false%}Overview{%elif  cid.0 == true%}ID: {{cid.1}}{%endif%}</title>
        <script src="/js/jquery-2.2.3.min.js" type="text/javascript"></script>        
        <script src="/js/backend.js" type="text/javascript"></script>             
        <style type="text/css">
        #AIcons:hover {cursor:pointer;}
        #AIcons img:hover {}
        
                
        #MainX {position:relative;left:5%; margin-left:-X;width:800px;top:50px;font-family:Arial;}
        #MainX ul{list-style-type: none;padding:0px;width:150px;}
        #MainX ul li {cursor:pointer;}
        #MainX ul li:hover {color:#ef2929;}
        
        #MainX #left {position:absolute;height:auto}
        #MainX #left ul li a {text-decoration: none;color:#000000}
        #MainX #left ul li a:hover {color:#ef2929;}
        #MainX #left .bcolor {color:#ef2929;}
        #MainX #right {position:absolute;left:200px;}
        #MainX #right button {border-style:solid;border-width:1px;border-color:#000000;cursor:pointer;}
        #MainX #right button:hover {border-style:dashed;border-width:2px;border-color:#ef2929;}
        </style>        
    </head>
    <body>
        <span id="AIcons">
        <img src="/img/logout.svg" width="20px" height="20">
        <img onclick="BackendObj.Add();" src="/img/new.svg" width="20px" height="20">
        </span>
                                        
        <div id="MainX">                                                
            <div id="left" style="border-style: solid;border-width: 1px;">
            <div style="padding: 10px;">            
            <b>generated codes</b><br>
            <span>                        
            {%if codes.0 == false%}
            -- NO Codes generated --            
            {%elif codes.0 == true%}
            <ul>
                {%for cdx in codes.1%}
                <li><a {%if cid.0 == true%}class="bcolor"{%endif%} href="/backend/code/{{cdx}}">{{cdx}}</a></li>                
                {%endfor%}                
            </ul>
            {%endif%}
            </span>            
            </div>
            </div>
                    
            <div id="right">
                {% block stuff %}
                {% endblock %}                  
            </div>            
        </div>                          
    </body>
</html>