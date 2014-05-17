"""
 Base class for testing syncing algorithm

 (c) 2013-2014 by Mega Limited, Wellsford, New Zealand

 This file is part of the MEGA SDK - Client Access Engine.

 Applications using the MEGA API must present a valid application key
 and comply with the the rules set forth in the Terms of Service.

 The MEGA SDK is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

 @copyright Simplified (2-clause) BSD License.

 You should have received a copy of the license along with this
 program.
"""

# TODO tests:
# * "pause" sync
# * lock directory
# * exotic filenames
# * large (> 4Gb) files

from sync_test_base import SyncTestBase
import random
import os
import logging

class SyncTest(SyncTestBase):
    """
    Class with MEGA SDK test methods
    """

# tests
    def test_create_delete_files(self):
        """
        create files with different size,
        compare files on both folders,
        remove files, check that files removed from the second folder
        """
        logging.info("Launching test_create_delete_files test")
        self.assertTrue(self.app.is_alive(), "Test application is not running")

        # make sure remote folders are empty
        self.assertTrue(self.dirs_check_empty(), "Checking if remote folders are empty")
        self.assertTrue(self.app.is_alive(), "Test application is not running")

        # create files
        l_files = self.files_create()
        self.assertIsNotNone(l_files, "Creating files")
        self.assertTrue(self.app.is_alive(), "Test application is not running")

        self.app.sync()

        # comparing
        self.assertTrue(self.files_check(l_files), "Comparing files")
        self.assertTrue(self.app.is_alive(), "Test application is not running")

        # remove files
        self.assertTrue(self.files_remove(l_files), "Removing files")
        self.assertTrue(self.app.is_alive(), "Test application is not running")

        # make sure remote folders are empty
        self.assertTrue(self.dirs_check_empty(), "Checking if remote folders are empty")
        self.assertTrue(self.app.is_alive(), "Test application is not running")

        return True

    def test_create_rename_delete_files(self):
        """
        create files with different size,
        compare files on both folders,
        rename files
        """
        logging.info("Launching test_create_rename_delete_files test")
        self.assertTrue(self.app.is_alive(), "Test application is not running")

        # make sure remote folders are empty
        self.assertTrue(self.dirs_check_empty(), "Checking if remote folders are empty")
        self.assertTrue(self.app.is_alive(), "Test application is not running")

        # create files
        l_files = self.files_create()
        self.assertIsNotNone(l_files, "Creating files")
        self.assertTrue(self.app.is_alive(), "Test application is not running")

        self.app.sync()

        # comparing
        self.assertTrue(self.files_check(l_files), "Comparing files")
        self.assertTrue(self.app.is_alive(), "Test application is not running")

        # renaming
        self.assertTrue(self.files_rename(l_files), "Renaming files")
        self.assertTrue(self.app.is_alive(), "Test application is not running")

        self.app.sync()

        # comparing
        self.assertTrue(self.files_check(l_files), "Comparing files")
        self.assertTrue(self.app.is_alive(), "Test application is not running")

        # remove files
        self.assertTrue(self.files_remove(l_files), "Removing files")
        self.assertTrue(self.app.is_alive(), "Test application is not running")

        # make sure remote folders are empty
        self.assertTrue(self.dirs_check_empty(), "Checking if remote folders are empty")
        self.assertTrue(self.app.is_alive(), "Test application is not running")

        return True

    def test_create_delete_dirs(self):
        """
        create directories with different amount of files,
        compare directories on both sync folders,
        remove directories, check that directories removed from the second folder
        """
        logging.info("Launching test_create_delete_dirs test")
        self.assertTrue(self.app.is_alive(), "Test application is not running")

        # make sure remote folders are empty
        self.assertTrue(self.dirs_check_empty(), "Checking if remote folders are empty")
        self.assertTrue(self.app.is_alive(), "Test application is not running")

        # create dirs
        l_dirs = self.dirs_create()
        self.assertIsNotNone(l_dirs, "Creating directories")
        self.assertTrue(self.app.is_alive(), "Test application is not running")

        self.app.sync()

        # comparing
        self.assertTrue(self.dirs_check(l_dirs), "Comparing directories")
        self.assertTrue(self.app.is_alive(), "Test application is not running")

        # remove files
        self.assertTrue(self.dirs_remove(l_dirs), "Removing directories")
        self.assertTrue(self.app.is_alive(), "Test application is not running")

        # make sure remote folders are empty
        self.assertTrue(self.dirs_check_empty(), "Checking if remote folders are empty")
        self.assertTrue(self.app.is_alive(), "Test application is not running")

        return True

    def test_create_rename_delete_dirs(self):
        """
        create directories with different amount of files,
        compare directories on both sync folders,
        rename directories
        compare directories on both sync folders,
        remove directories, check that directories removed from the second folder
        """
        logging.info("Launching test_create_rename_delete_dirs test")
        self.assertTrue(self.app.is_alive(), "Test application is not running")

        # make sure remote folders are empty
        self.assertTrue(self.dirs_check_empty(), "Checking if remote folders are empty")
        self.assertTrue(self.app.is_alive(), "Test application is not running")

        # create dirs
        l_dirs = self.dirs_create()
        self.assertIsNotNone(l_dirs, "Creating directories")
        self.assertTrue(self.app.is_alive(), "Test application is not running")

        self.app.sync()

        # comparing
        self.assertTrue(self.dirs_check(l_dirs), "Comparing directories")
        self.assertTrue(self.app.is_alive(), "Test application is not running")

        # rename dirs
        self.assertTrue(self.dirs_rename(l_dirs), "Rename directories")
        self.assertTrue(self.app.is_alive(), "Test application is not running")

        self.app.sync()

        # comparing
        self.assertTrue(self.dirs_check(l_dirs), "Comparing directories")
        self.assertTrue(self.app.is_alive(), "Test application is not running")

        # remove files
        self.assertTrue(self.dirs_remove(l_dirs), "Removing directories")
        self.assertTrue(self.app.is_alive(), "Test application is not running")

        # make sure remote folders are empty
        self.assertTrue(self.dirs_check_empty(), "Checking if remote folders are empty")
        self.assertTrue(self.app.is_alive(), "Test application is not running")

        return True

    def test_sync_files_write(self):
        """
        write data to a file located in both sync folders
        check for the result, expected result: both files contains the same content
        """

        logging.info("Launching test_sync_files_write test")
        self.assertTrue(self.app.is_alive(), "Test application is not running")

        self.assertTrue(self.dirs_check_empty(), "Checking if remote folders are empty")
        self.assertTrue(self.app.is_alive(), "Test application is not running")

        for _ in range(0, 5):
            self.assertTrue(self.app.is_alive(), "Test application is not running")
            strlen = random.randint(10, 20)
            fname = self.get_random_str(size=strlen)

            fname_in = os.path.join(self.app.local_folder_in, fname)
            fname_out = os.path.join(self.app.local_folder_out, fname)

            logging.debug("Writing to both files: %s and %s" % (fname_in, fname_out))

            with open(fname_in, 'a'):
                os.utime(fname_in, None)
            with open(fname_out, 'a'):
                os.utime(fname_out, None)

            self.app.sync()

            for _ in range(10):
                with open(fname_in, 'a') as f_in:
                    f_in.write(self.get_random_str(100))

                with open(fname_out, 'a') as f_out:
                    f_out.write(self.get_random_str(100))

                self.app.sync()

            md5_in = self.md5_for_file(fname_in)
            md5_out = self.md5_for_file(fname_out)

            logging.debug("File %s md5: %s" % (fname_in, md5_in))
            logging.debug("File %s md5: %s" % (fname_out, md5_out))

            self.assertEqual(md5_in, md5_out, "Files do not match")

    def test_local_operations(self):
        """
        write data to a file located in both sync folders
        check for the result, expected result: both files contains the same content
        """
        self.assertTrue(self.app.is_alive(), "Test application is not running")
        l_tree = self.local_tree_create("", 5)
        self.assertIsNotNone(l_tree, "Failed to create directory tree!")
        self.assertTrue(self.app.is_alive(), "Test application is not running")
        self.app.sync()
        self.assertTrue(self.local_tree_compare(l_tree), "Failed to compare directory trees!")
        self.assertTrue(self.app.is_alive(), "Test application is not running")
        self.assertTrue(self.local_tree_create_and_move(l_tree), "Failed to create a new sub folder and move an existing directory into it!")
        self.assertTrue(self.app.is_alive(), "Test application is not running")
        self.assertTrue(self.local_tree_multiple_renames(l_tree), "Failed to rename folder multiple times and then rename back to the original name!")
        self.assertTrue(self.app.is_alive(), "Test application is not running")

