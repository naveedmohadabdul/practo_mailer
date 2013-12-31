
<!DOCTYPE html>
<html>
<head>
<title>Practo</title>
</head>
<body>
<h1>Welcome to the Practo App</h1>
<ul>
</ul>
<p>
<form action="/body_filter" method="POST">
<h3>Practo patient data</h3>
Select patients to mail...
<table>
<tr>
%for i in items:
%x=i
%end
<th></th>
%for item in items[x][0]:
<th>{{item}}</th>
%end
</tr>
%a = 0
%for i in items:
%for j in items[i]: 
<tr>
<td>
%if len(j['email'])>0:
<input type="checkbox" name="email" size="40" value="{{j['email']+"XXX"+j['name']}}">
%else:
<input type="checkbox" name="email" size="40" value="{{j['email']+"XXX"+j['name']}}" disabled>
<br>
</td>
%end
%for k in j:
<td>{{j[k]}}</td>
%end
</tr>
%end
%end
<tr>
<th>
<input type="submit" name="Mail" value="Mail">
</th>
</tr>
</table>
</form>
</body>
</html>
