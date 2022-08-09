<?
  $flag = "FLAG{THIS_IS_LOCAL_FAG}";
  if(isset($_GET['url'])) $url = $_GET['url'];
  if($url){
    system("ping -c 2 ".$url." 2>&1");
  }
?>
