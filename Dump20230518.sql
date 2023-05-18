CREATE DATABASE  IF NOT EXISTS `segundok` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `segundok`;
-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: segundok
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `estudiante`
--

DROP TABLE IF EXISTS `estudiante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estudiante` (
  `cedula` varchar(12) NOT NULL,
  `nombres` varchar(20) NOT NULL,
  `apellidos` varchar(20) NOT NULL,
  `correo` varchar(45) NOT NULL,
  `cod_mat` int NOT NULL,
  `estado` varchar(1) NOT NULL,
  `id_usuario` varchar(20) NOT NULL,
  `carrera` varchar(45) NOT NULL,
  PRIMARY KEY (`cedula`),
  KEY `id_usuario` (`id_usuario`),
  CONSTRAINT `estudiante_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estudiante`
--

LOCK TABLES `estudiante` WRITE;
/*!40000 ALTER TABLE `estudiante` DISABLE KEYS */;
INSERT INTO `estudiante` VALUES ('0987654321','ANA PAULA','ORELLANA CASTRO','orellana@hotmail.com',222,'A','erick23','ANALISIS DE DATOS'),('0987667890','JOSUE EULALIO','AMADOR ','amador@gmail.com',2233,'A','ariel23','ANALISIS DE DATOS'),('1214334343','JOSUE JUSTIN','AMADOR CASTRO','amador@gmail.com',123,'I','gabriela23','DESARROLLO DE SOFTWARE'),('1234554321','MIRIAM ANA','LUQUE PEREZ','perez@gmail.com',333,'A','victor23','MARKETTING'),('1234567890','RAUL ENRIQUE','TORRES MOREIRA','mora@gmail.com',111,'I','ariel23','ANALISIS DE DATOS'),('1234567891','ARIEL JAVIER','ASUNCION ZURITA','asuncion@istg.edu.ec',111,'A','ariel23','DESARROLLO DE SOFTWARE');
/*!40000 ALTER TABLE `estudiante` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `usuario` varchar(20) NOT NULL,
  `password` varchar(35) NOT NULL,
  `nombres` varchar(45) NOT NULL,
  `apellidos` varchar(45) NOT NULL,
  `correo` varchar(45) NOT NULL,
  `profesion` varchar(25) NOT NULL,
  `estado` varchar(1) NOT NULL,
  PRIMARY KEY (`usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES ('ariel23','12345','ARIEL AGUSTIN','ASUNCION ZURITA','ariel@gmail.com','DESARROLLADOR','A'),('arteaga11','3333','VALESKA','ARTEAGA','brithany@hotmail.com','DESARROLLADORA','A'),('biggoMa','1234','biggo','maggi ma','biggo@gmail.com','Contador','A'),('deso34','12345','ROBERTO LUIS','PEREZ LUQUE','perez@hotmail.com','Contador','A'),('erick23','55555','ERICK JAIR','ARCE PAREDES','erick@outlook.com','LIDER','A'),('gabriela23','12345','GABRIELA MIREYA','TORRES ORTIZ','gabriela@gmail.com','LIDER','A'),('hola456','xxxxx','JOSE ENRIQUE','SOTO','jose@gmail.com','Desarrollador','A'),('ibarra23','7777','RENATO','IBARRA','ibarra@gmail.com','FUTBOLISTA','A'),('victor23','11111','VICTOR ALFONSO','CASTRO PARRALES','victor@hotmail.com','ANALISTA','A');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-18 12:07:44
