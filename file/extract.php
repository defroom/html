<?php
        $a = "student";
        $my_array = array("a" => "cat", "b" => "Dog", "c" => "horse");
        extract($my_array, EXTR_PREFIX_SAME, "dup" );
        echo "\$a = $a; \$b = $b; \$c =$c; \$dup_a = $dup_a";
?>