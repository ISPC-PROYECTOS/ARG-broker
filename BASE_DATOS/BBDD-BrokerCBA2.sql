CREATE DATABASE  IF NOT EXISTS `brokercba` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `brokercba`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: brokercba
-- ------------------------------------------------------
-- Server version	8.0.37

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
-- Table structure for table `accion`
--

DROP TABLE IF EXISTS `accion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accion` (
  `id_accion` int NOT NULL AUTO_INCREMENT,
  `nombre_accion` varchar(45) DEFAULT NULL,
  `simbolo_accion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_accion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accion`
--

LOCK TABLES `accion` WRITE;
/*!40000 ALTER TABLE `accion` DISABLE KEYS */;
/*!40000 ALTER TABLE `accion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `broker`
--

DROP TABLE IF EXISTS `broker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `broker` (
  `id_comision` int NOT NULL AUTO_INCREMENT,
  `id_num_transaccion` int NOT NULL,
  `comision` float DEFAULT NULL,
  PRIMARY KEY (`id_comision`),
  KEY `id_num_transaccion_idx` (`id_num_transaccion`),
  CONSTRAINT `id_num_transaccion` FOREIGN KEY (`id_num_transaccion`) REFERENCES `transaccion` (`id_num_transaccion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `broker`
--

LOCK TABLES `broker` WRITE;
/*!40000 ALTER TABLE `broker` DISABLE KEYS */;
/*!40000 ALTER TABLE `broker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacion`
--

DROP TABLE IF EXISTS `cotizacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cotizacion` (
  `id_cotizacion_accion` int NOT NULL AUTO_INCREMENT,
  `id_accion` int NOT NULL,
  `fecha_hora` datetime(6) DEFAULT NULL,
  `precio_venta` float DEFAULT NULL,
  `precio_compra` float DEFAULT NULL,
  PRIMARY KEY (`id_cotizacion_accion`),
  KEY `id_accion_idx` (`id_accion`),
  CONSTRAINT `id_accion` FOREIGN KEY (`id_accion`) REFERENCES `accion` (`id_accion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacion`
--

LOCK TABLES `cotizacion` WRITE;
/*!40000 ALTER TABLE `cotizacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `cotizacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inversor`
--

DROP TABLE IF EXISTS `inversor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inversor` (
  `id_tipo_inversor` int NOT NULL,
  `cuit_o_cuil` bigint NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `apellido` varchar(45) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `contrasena` varchar(45) DEFAULT NULL,
  `fecha_alta_inversor` date DEFAULT NULL,
  `saldo_inicial` int DEFAULT NULL,
  PRIMARY KEY (`cuit_o_cuil`),
  KEY `cuit_o_cuil` (`cuit_o_cuil`),
  KEY `id_tipo_inversor` (`id_tipo_inversor`),
  CONSTRAINT `id_tipo_inversor` FOREIGN KEY (`id_tipo_inversor`) REFERENCES `tipo_inversor` (`id_tipo_inversor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inversor`
--

LOCK TABLES `inversor` WRITE;
/*!40000 ALTER TABLE `inversor` DISABLE KEYS */;
INSERT INTO `inversor` VALUES (0,27123456780,'Pedro','Juarez','pepe@gmail.com','Pepe123!','2024-10-17',1000000),(1,27123456789,'Hebe','Pereyra','hebepereyra@gmail.com','Hebep!33','2024-10-18',1000000),(0,27134574289,'Adriana','Moral','agmoral@gmail.com','Agmoral!57','2024-10-17',1000000),(1,27395460094,'Victoria','Picco','vpicco@gmail.com','Vicki37!','2024-10-17',1000000),(0,27541927420,'Magdalena','Picco','magda@gmail.com','Magda16!','2024-10-17',1000000);
/*!40000 ALTER TABLE `inversor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_inversor`
--

DROP TABLE IF EXISTS `tipo_inversor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_inversor` (
  `id_tipo_inversor` int NOT NULL,
  `tipo_inversor` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`id_tipo_inversor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_inversor`
--

LOCK TABLES `tipo_inversor` WRITE;
/*!40000 ALTER TABLE `tipo_inversor` DISABLE KEYS */;
INSERT INTO `tipo_inversor` VALUES (0,'fisica'),(1,'juridica');
/*!40000 ALTER TABLE `tipo_inversor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_transaccion`
--

DROP TABLE IF EXISTS `tipo_transaccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_transaccion` (
  `id_tipo_transaccion` int NOT NULL AUTO_INCREMENT,
  `tipo_transaccion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_tipo_transaccion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_transaccion`
--

LOCK TABLES `tipo_transaccion` WRITE;
/*!40000 ALTER TABLE `tipo_transaccion` DISABLE KEYS */;
/*!40000 ALTER TABLE `tipo_transaccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaccion`
--

DROP TABLE IF EXISTS `transaccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transaccion` (
  `id_num_transaccion` int NOT NULL AUTO_INCREMENT,
  `id_tipo_transaccion` int NOT NULL,
  `cuit_o_cuil` int NOT NULL,
  `id_cotizacion_accion` int NOT NULL,
  `cantidad_acciones_transaccion` float DEFAULT NULL,
  `fecha_hora_transaccion` datetime(6) DEFAULT NULL,
  `valor_transaccion` float DEFAULT NULL,
  PRIMARY KEY (`id_num_transaccion`),
  KEY `cuit_o_cuil_idx` (`cuit_o_cuil`) /*!80000 INVISIBLE */,
  KEY `id_cotizacion_accion_idx` (`id_cotizacion_accion`),
  KEY `id_tipo_transaccion_idx` (`id_tipo_transaccion`) /*!80000 INVISIBLE */,
  CONSTRAINT `id_cotizacion_accion` FOREIGN KEY (`id_cotizacion_accion`) REFERENCES `cotizacion` (`id_cotizacion_accion`),
  CONSTRAINT `id_num_inversor` FOREIGN KEY (`cuit_o_cuil`) REFERENCES `inversor` (`id_tipo_inversor`),
  CONSTRAINT `id_tipo_transaccion` FOREIGN KEY (`id_tipo_transaccion`) REFERENCES `tipo_transaccion` (`id_tipo_transaccion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaccion`
--

LOCK TABLES `transaccion` WRITE;
/*!40000 ALTER TABLE `transaccion` DISABLE KEYS */;
/*!40000 ALTER TABLE `transaccion` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
