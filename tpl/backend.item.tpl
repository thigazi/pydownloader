{% extends "backend.tpl" %}
{% block stuff %}
<b>Filelist</b><br>
Anzahl der Dateien in der DB: 10
<form accept-charset="UTF-8" style="margin-bottom: 10px;">
    <table>
        <thead></thead>
        <tbody>
            <tr><td>MeineDatei.zip</td><td>Downloads: <select><option value="0">1</option><option value="1">1</option><option selected="selected" value="2">2</option><option value="3">3</option><option value="4">4</option><option value="5">5</option></select></td><td><img src="/img/delete.svg" width="20px" height="20"></td></tr>
        </tbody>
    </table>
    <input type="file" />
</form>
<span><button>L&ouml;sche Code</button></span>
{% endblock %}