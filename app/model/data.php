<?php 
    class database{
        private $conn;
        function __construct(){
            $this->conn = new mysqli("localhost", "root", "", "Lave");
            if ($this->conn->connect_error) {
                die("Connection failed: " . $this->conn->connect_error);
            }
        }
    }

    class data{
        private $db;
        function __construct(){
            $this->db = new database();
        }
        function get_data(){
            $query = "SELECT * FROM $table";
            $result = $this->db->conn->query($query);
            while($row = $result->fetch_assoc()){
                echo $row['name'];
            }
        }
    }
    