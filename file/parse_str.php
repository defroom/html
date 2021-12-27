<?php
        $user = "lisi";
        parse_str("user=zhangsan&pass=123", $users);
        var_dump($user);
        echo "<br/>";
        var_dump($pass);
        echo "<br/>";
        var_dump($users);
?>