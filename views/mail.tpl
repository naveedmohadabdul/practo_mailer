<!DOCTYPE html>
<html>
<body>
<p>Mass mailer requires your Gmail access credentials for sending mails</p>
<form action="/mass_mail" method="POST">
<table>
<tr><td>Username: <input type="text" name="name" value=""><br></td><tr>
<tr><td>Password:<input type="password" name="password" value=""><br></td><tr>
<tr><td>FromAddr:<input type="text" name="fromaddr" value=""><br></td><tr>
<tr><td>Mail To : <input type="text"  name="P_Email" value={{','.join(str(e) for e in emails.values())}} disabled></td><br><tr>
<tr><td><input type="hidden" name="P_UID" value={{','.join(str(e) for e in emails.keys())}}><br></td><tr>
<tr><td>Subject<td></tr>
<tr><td><input type="text" name="subject" size="215" maxlength="1000" style="height:25px;"></td></tr>
<tr><td>Message</td></tr>
<tr><td><TEXTAREA name="message" size="215" rows="10" cols="163" style="height:100px;"></TEXTAREA></td></tr>
<tr><td><input type="submit" value="Submit"></td>
</form>
</body>
</html>

