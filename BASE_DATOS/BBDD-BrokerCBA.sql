-- MySQL Script generated by MySQL Workbench
-- Sun Oct 20 09:42:47 2024
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';



-- -----------------------------------------------------
-- Schema BrokerCBA
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `BrokerCBA` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;

USE `BrokerCBA` ;

-- -----------------------------------------------------
-- Table `BrokerCBA`.`tipo_inversor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BrokerCBA`.`tipo_inversor` (
  `id_tipo_inversor` INT NOT NULL,
  `tipo_inversor` VARCHAR(45) NULL,
  PRIMARY KEY (`id_tipo_inversor`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BrokerCBA`.`inversor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BrokerCBA`.`inversor` (
  `id_tipo_inversor` INT NOT NULL,
  `cuit_o_cuil` VARCHAR(11) NOT NULL,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `email` VARCHAR(200) NULL,
  `contrasena` VARCHAR(45) NULL,
  `fecha_alta_inversor` DATE NULL,
  `saldo_inicial` INT NULL,
  PRIMARY KEY (`cuit_o_cuil`),
  INDEX `cuit_o_cuil` (`cuit_o_cuil` ASC) VISIBLE,
  CONSTRAINT `id_tipo_inversor`
    FOREIGN KEY (`id_tipo_inversor`)
    REFERENCES `BrokerCBA`.`tipo_inversor` (`id_tipo_inversor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BrokerCBA`.`accion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BrokerCBA`.`accion` (
  `id_accion` INT NOT NULL AUTO_INCREMENT,
  `nombre_accion` VARCHAR(45) NULL,
  `simbolo_accion` VARCHAR(45) NULL,
  PRIMARY KEY (`id_accion`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BrokerCBA`.`cotizacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BrokerCBA`.`cotizacion` (
  `id_cotizacion_accion` INT NOT NULL AUTO_INCREMENT,
  `id_accion` INT NOT NULL,
  `fecha_hora` DATETIME(6) NULL,
  `precio_venta` FLOAT NULL,
  `precio_compra` FLOAT NULL,
  PRIMARY KEY (`id_cotizacion_accion`),
  INDEX `id_accion_idx` (`id_accion` ASC) VISIBLE,
  CONSTRAINT `id_accion`
    FOREIGN KEY (`id_accion`)
    REFERENCES `BrokerCBA`.`accion` (`id_accion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
ALTER TABLE `BrokerCBA`.`cotizacion`  
ADD cantidad_disponible INT;

-- -----------------------------------------------------
-- Table `BrokerCBA`.`tipo_transaccion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BrokerCBA`.`tipo_transaccion` (
  `id_tipo_transaccion` INT NOT NULL AUTO_INCREMENT,
  `tipo_transaccion` VARCHAR(45) NULL,
  PRIMARY KEY (`id_tipo_transaccion`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BrokerCBA`.`transaccion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BrokerCBA`.`transaccion` (
  `id_num_transaccion` INT NOT NULL AUTO_INCREMENT,
  `id_tipo_transaccion` INT NOT NULL,
  `cuit_o_cuil` VARCHAR(11) NOT NULL,
  `id_cotizacion_accion` INT NOT NULL,
  `cantidad_acciones_transaccion` FLOAT NULL,
  `fecha_hora_transaccion` DATETIME(6) NULL,
  `valor_transaccion` FLOAT NULL,
  PRIMARY KEY (`id_num_transaccion`),
  INDEX `cuit_o_cuil_idx` (`cuit_o_cuil` ASC) INVISIBLE,
  INDEX `id_cotizacion_accion_idx` (`id_cotizacion_accion` ASC) VISIBLE,
  INDEX `id_tipo_transaccion_idx` (`id_tipo_transaccion` ASC) INVISIBLE,
  CONSTRAINT `cuit_o_cuil`
    FOREIGN KEY (`cuit_o_cuil`)
    REFERENCES `BrokerCBA`.`inversor` (`cuit_o_cuil`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `id_cotizacion_accion`
    FOREIGN KEY (`id_cotizacion_accion`)
    REFERENCES `BrokerCBA`.`cotizacion` (`id_cotizacion_accion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `id_tipo_transaccion`
    FOREIGN KEY (`id_tipo_transaccion`)
    REFERENCES `BrokerCBA`.`tipo_transaccion` (`id_tipo_transaccion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
-- -----------------------------------------------------
-- Table `BrokerCBA`.`broker`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BrokerCBA`.`broker` (
  `id_comision` INT NOT NULL AUTO_INCREMENT,
  `id_num_transaccion` INT NOT NULL,
  `comision` FLOAT NULL,
  PRIMARY KEY (`id_comision`),
  INDEX `id_num_transaccion_idx` (`id_num_transaccion` ASC) VISIBLE,
  CONSTRAINT `id_num_transaccion`
    FOREIGN KEY (`id_num_transaccion`)
    REFERENCES `BrokerCBA`.`transaccion` (`id_num_transaccion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
