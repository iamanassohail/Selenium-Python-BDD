from selenium import webdriver
from features.pages.BasePage import BasePage
from utilities import ConfigReader


def before_all(self):
    BasePage.define_driver(self)


def after_all(self):
    BasePage.quit_driver(self)
