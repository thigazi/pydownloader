<!DOCTYPE HTML>
<html>
	<head>
		<title>Code Eingabe</title>		
		<style type="text/css">
			html, body, div, span, applet, object, iframe,h1, h2, h3, h4, h5, h6, p, blockquote, pre,a, abbr, acronym, address, big, cite, code,del, dfn, em, img, ins, kbd, q, s, samp,small, strike, strong, sub, sup, tt, var,b, u, i, center,dl, dt, dd, ol, ul, li,fieldset, form, label, legend,table, caption, tbody, tfoot, thead, tr, th, td,article, aside, canvas, details, embed, figure, figcaption, footer, header, hgroup, menu, nav, output, ruby, section, summary, time, mark, audio, video {margin: 0;padding: 0;border: 0;font-size: 100%;font: inherit;vertical-align: baseline;}
			article, aside, details, figcaption, figure,
			footer, header, hgroup, menu, nav, section {display: block;}
			body {line-height: 1;}ol, ul {list-style: none;}blockquote, q {quotes: none;}
			blockquote:before, blockquote:after,
			q:before, q:after {content: '';content: none;}
			table {border-collapse: collapse;border-spacing: 0;}
			#boxx {position:relative;display:block;left:45%;top:100px;width:300px;}
			#boxx table tr {font-family:Arial;}			
		</style>		
	</head>
	<body>
		<div id="boxx">
			<form name="fsubmitx" method="post">
			<table>
			<tr><td>One-Time-Code:</td><td><input type="password" name="otpass" maxlength="10" /></td></tr>						
			</table>
			</form>
			<button onclick="document.fsubmitx.submit();" value="Senden!">Senden!</button>			
		</div>
					
	</body>	
</html>
