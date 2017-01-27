<!DOCTYPE HTML>
<html>
	<head>
		<title>Login Area</title>		
		<style type="text/css">
			html, body, div, span, applet, object, iframe,h1, h2, h3, h4, h5, h6, p, blockquote, pre,a, abbr, acronym, address, big, cite, code,del, dfn, em, img, ins, kbd, q, s, samp,small, strike, strong, sub, sup, tt, var,b, u, i, center,dl, dt, dd, ol, ul, li,fieldset, form, label, legend,table, caption, tbody, tfoot, thead, tr, th, td,article, aside, canvas, details, embed, figure, figcaption, footer, header, hgroup, menu, nav, output, ruby, section, summary, time, mark, audio, video {margin: 0;padding: 0;border: 0;font-size: 100%;font: inherit;vertical-align: baseline;}
			article, aside, details, figcaption, figure,
			footer, header, hgroup, menu, nav, section {display: block;}
			body {line-height: 1;}ol, ul {list-style: none;}blockquote, q {quotes: none;}
			blockquote:before, blockquote:after,
			q:before, q:after {content: '';content: none;}
			table {border-collapse:separate;border-spacing: 5px;}
			#boxx {position:relative;display:block;left:45%;top:100px;width:300px;}
			#boxx table tr {font-family:Arial;}
			#boxx table tr input {font-family:Arial;}
			.rahmen {border-style:solid;border-width:1px;border-color:#000000;}
			#boxx div {position:relative;display:block;left:35%;}
			#boxx span {margin-top:15px;position:absolute;font-family:Arial}
		</style>
		<script src="/js/jquery-2.2.3.min.js" type="text/javascript"></script>
		<script src="/js/jquery.session.js" type="text/javascript"></script>
		<script src="/js/start.js" type="text/javascript"></script>		
	</head>
	<body>
		<div id="boxx">
			<form name="LArea" id="LArea" method="post">
			<table>
			<tr><td>Login:</td><td><input class="rahmen" type="text" name="credentials" maxlength="10" /></td></tr>
			<tr><td>Pass:</td><td><input class="rahmen" type="password" name="credentials" maxlength="10" /></td></tr>						
			</table>
			</form>
			<div>
			    <button class="rahmen" onclick="document.LArea.submit();" value="Senden!">Login!</button>			    			    
			</div>			
			<span id="emsg"></span>
		</div>
		{%if setpass%}
		<span style="position:relative;top: 120px;left:40%;font-family: Arial">Create a new Login and Password for the 1st Account</span>
		{%endif%}
	</body>	
</html>