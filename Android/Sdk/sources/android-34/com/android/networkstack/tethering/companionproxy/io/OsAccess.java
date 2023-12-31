package com.android.networkstack.tethering.companionproxy.io;

import android.os.ParcelFileDescriptor;
import android.system.StructPollfd;

import java.io.FileDescriptor;
import java.io.IOException;

/**
 * Provides access to all relevant OS functions..
 *
 * @hide
 */
public abstract class OsAccess {
    /** Closes the given file, suppressing IO exceptions. */
    public abstract void close(ParcelFileDescriptor fd);

    /** Returns file name for debugging purposes. */
    public abstract String getFileDebugName(ParcelFileDescriptor fd);

    /** Returns inner FileDescriptor instance. */
    public abstract FileDescriptor getInnerFileDescriptor(ParcelFileDescriptor fd);

    /**
     * Reads available data from the given non-blocking file descriptor.
     *
     * Returns zero if there's no data to read at this moment.
     * Returns -1 if the file has reached its end or the input stream has been closed.
     * Otherwise returns the number of bytes read.
     */
    public abstract int read(FileDescriptor fd, byte[] buffer, int pos, int len)
            throws IOException;

    /**
     * Writes data into the given non-blocking file descriptor.
     *
     * Returns zero if there's no buffer space to write to at this moment.
     * Otherwise returns the number of bytes written.
     */
    public abstract int write(FileDescriptor fd, byte[] buffer, int pos, int len)
            throws IOException;

    public abstract long monotonicTimeMillis();
    public abstract void setNonBlocking(FileDescriptor fd) throws IOException;
    public abstract ParcelFileDescriptor[] pipe() throws IOException;

    public abstract int poll(StructPollfd[] fds, int timeoutMs) throws IOException;
    public abstract short getPollInMask();
    public abstract short getPollOutMask();
}
