# Fied nad file extention

exec{'fix-wordpress':
    command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path     => '/bin/';
}
