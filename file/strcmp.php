<?php
    $password1 = 123;
    $password2 = "123a";

    if (strcmp($password1, $password2) == 0){
            echo "strcmp equl!";
        }else{
            echo"strcmp unequl!";
        }
        echo"<br/>";
      if ($password1 == $password2){
            echo "strcmp equl!";
        }else{
            echo"strcmp unequl!";
        }
?>