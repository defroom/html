<?php
        $users = array("01"=>"zhangsan","02"=>"lisi","03"=>"123");
        $colors = array("red","green","blue");
        foreach($users as $value){
                echo $value."<br/>";
                }
        foreach($colors as $key=>$value){
                echo "$key=>$value"."<br/>";
                }